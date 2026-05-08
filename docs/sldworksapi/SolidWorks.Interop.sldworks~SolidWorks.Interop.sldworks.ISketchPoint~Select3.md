# Select3 Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select3`

Obsolete. Superseded by ISketchPoint::Select4.
Obsolete. Superseded by [ISketchPoint::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select3( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout _
) As System.Boolean
```

```

Dim instance As ISketchPoint
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim value As System.Boolean
 
value = instance.Select3(Append, Mark, Callout)
```

```

System.bool Select3( 
   System.bool Append,
   System.int Mark,
   Callout Callout
)
```

```

System.bool Select3( 
   System.bool Append,
   System.int Mark,
   Callout^ Callout
) 
```

#### Parameters

*Append*

*Mark*

*Callout*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)
