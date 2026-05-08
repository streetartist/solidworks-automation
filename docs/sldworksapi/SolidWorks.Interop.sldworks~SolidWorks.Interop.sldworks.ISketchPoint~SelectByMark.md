# SelectByMark Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~SelectByMark`

Obsolete. Superseded by ISketchPoint::Select4.
Obsolete. Superseded by [ISketchPoint::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByMark( _
   ByVal AppendFlag As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchPoint
Dim AppendFlag As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByMark(AppendFlag, Mark)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
) 
```

#### Parameters

*AppendFlag*

*Mark*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)
