# SetSketchEditable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetSketchEditable`

Sets whether this sketch is editable.
Sets whether this sketch is editable.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSketchEditable( _
   ByVal Editable As System.Boolean _
) 
```

```

Dim instance As ISketch
Dim Editable As System.Boolean
 
instance.SetSketchEditable(Editable)
```

```

void SetSketchEditable( 
   System.bool Editable
)
```

```

void SetSketchEditable( 
   System.bool Editable
) 
```

#### Parameters

*Editable*
:   True to make this sketch editable, false to make it read only

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IsSketchEditable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsSketchEditable.md)
