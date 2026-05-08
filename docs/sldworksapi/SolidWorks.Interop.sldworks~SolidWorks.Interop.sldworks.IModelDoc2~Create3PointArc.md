# Create3PointArc Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Create3PointArc`

Obsolete. Superseded by ISketchManager::Create3PointArc.
Obsolete. Superseded by [ISketchManager::Create3PointArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Create3PointArc( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal P3x As System.Double, _
   ByVal P3y As System.Double, _
   ByVal P3z As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim P3x As System.Double
Dim P3y As System.Double
Dim P3z As System.Double
Dim value As System.Boolean
 
value = instance.Create3PointArc(P1x, P1y, P1z, P2x, P2y, P2z, P3x, P3y, P3z)
```

```

System.bool Create3PointArc( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
)
```

```

System.bool Create3PointArc( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
) 
```

#### Parameters

*P1x*
:   X value of point 1

*P1y*
:   Y value of point 1

*P1z*
:   Z value of point 1

*P2x*
:   X value of point 2

*P2y*
:   Y value of point 2

*P2z*
:   Z value of point 2

*P3x*
:   X value of point 3

*P3y*
:   Y value of point 3

*P3z*
:   Z value of point 3

#### Return Value

True if successfully created, false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.md)  
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.md)  
[IModelDoc2::CreateTangentArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateTangentArc2.md)  
[IModelDoc2::ICreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc2.md)
