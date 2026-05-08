# SketchFillet2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchFillet2`

Obsolete. Superseded by ISketchManager::CreateFillet.
Obsolete. Superseded by [ISketchManager::CreateFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateFillet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchFillet2( _
   ByVal Rad As System.Double, _
   ByVal ConstrainedCorners As System.Short _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Rad As System.Double
Dim ConstrainedCorners As System.Short
Dim value As System.Boolean
 
value = instance.SketchFillet2(Rad, ConstrainedCorners)
```

```

System.bool SketchFillet2( 
   System.double Rad,
   System.short ConstrainedCorners
)
```

```

System.bool SketchFillet2( 
   System.double Rad,
   System.short ConstrainedCorners
) 
```

#### Parameters

*Rad*
:   Radius of the fillet in meters

*ConstrainedCorners*
:   Action to take if the corner to be filleted is constrained or has a dimension  (see **Remarks**)

#### Return Value

True if the fillet is created, false if not

Remarks

The ConstrainedCorners argument:

- Indicates what action to take if the corner to be filleted is constrained in some manner or has a dimension related to it. In this case, adding a fillet to the corner cannot be done without certain consequences. If the corner is not involved with any constraints, this argument is ignored.
- Can take one of the values found in [swConstrainedCornerAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedCornerAction_e.html).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
