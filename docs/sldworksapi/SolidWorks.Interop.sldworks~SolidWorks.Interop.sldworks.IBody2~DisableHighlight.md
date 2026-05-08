# DisableHighlight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisableHighlight`

Disables highlighting of the selected body in the graphics area.
Disables highlighting of the selected body in the graphics area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisableHighlight As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
instance.DisableHighlight = value
 
value = instance.DisableHighlight
```

```

System.bool DisableHighlight {get; set;}
```

```

property System.bool DisableHighlight {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to disable highlighting, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
