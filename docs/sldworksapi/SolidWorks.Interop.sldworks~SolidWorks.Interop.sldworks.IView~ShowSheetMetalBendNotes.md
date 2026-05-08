# ShowSheetMetalBendNotes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes`

Gets or sets whether to show sheet metal bend notes.
Gets or sets whether to show sheet metal bend notes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowSheetMetalBendNotes As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.ShowSheetMetalBendNotes = value
 
value = instance.ShowSheetMetalBendNotes
```

```

System.bool ShowSheetMetalBendNotes {get; set;}
```

```

property System.bool ShowSheetMetalBendNotes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show sheet metal bend notes, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
