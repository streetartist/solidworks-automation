# SketchChamfer Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchChamfer`

Obsolete. Superseded by ISketchManager::CreateChamfer.
Obsolete. Superseded by [ISketchManager::CreateChamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateChamfer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchChamfer( _
   ByVal AngleORdist As System.Double, _
   ByVal Dist1 As System.Double, _
   ByVal Options As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim AngleORdist As System.Double
Dim Dist1 As System.Double
Dim Options As System.Integer
 
instance.SketchChamfer(AngleORdist, Dist1, Options)
```

```

void SketchChamfer( 
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

```

void SketchChamfer( 
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
) 
```

#### Parameters

*AngleORdist*
:   Angle of the chamfer if using the Angle-Distance option or the distance of the second distance if using the Distance-Distance option

*Dist1*
:   Distance of the chamfer

*Options*
:   0 = Angle - Distance Chamfer

    1 = Distance - Distance Chamfer

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
