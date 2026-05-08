# PromptText Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PromptText`

Gets and sets the message prompt text.
Gets and sets the message prompt text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PromptText As System.String
```

```

Dim instance As INote
Dim value As System.String
 
instance.PromptText = value
 
value = instance.PromptText
```

```

System.string PromptText {get; set;}
```

```

property System.String^ PromptText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text to use in prompt message

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
