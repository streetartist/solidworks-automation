# InsertRefPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRefPlane`

Inserts a constraint-based reference plane using the selected reference entities.
Inserts a constraint-based reference plane using the selected reference entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRefPlane( _
   ByVal FirstConstraint As System.Integer, _
   ByVal FirstConstraintAngleOrDistance As System.Double, _
   ByVal SecondConstraint As System.Integer, _
   ByVal SecondConstraintAngleOrDistance As System.Double, _
   ByVal ThirdConstraint As System.Integer, _
   ByVal ThirdConstraintAngleOrDistance As System.Double _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim FirstConstraint As System.Integer
Dim FirstConstraintAngleOrDistance As System.Double
Dim SecondConstraint As System.Integer
Dim SecondConstraintAngleOrDistance As System.Double
Dim ThirdConstraint As System.Integer
Dim ThirdConstraintAngleOrDistance As System.Double
Dim value As System.Object
 
value = instance.InsertRefPlane(FirstConstraint, FirstConstraintAngleOrDistance, SecondConstraint, SecondConstraintAngleOrDistance, ThirdConstraint, ThirdConstraintAngleOrDistance)
```

```

System.object InsertRefPlane( 
   System.int FirstConstraint,
   System.double FirstConstraintAngleOrDistance,
   System.int SecondConstraint,
   System.double SecondConstraintAngleOrDistance,
   System.int ThirdConstraint,
   System.double ThirdConstraintAngleOrDistance
)
```

```

System.Object^ InsertRefPlane( 
   System.int FirstConstraint,
   System.double FirstConstraintAngleOrDistance,
   System.int SecondConstraint,
   System.double SecondConstraintAngleOrDistance,
   System.int ThirdConstraint,
   System.double ThirdConstraintAngleOrDistance
) 
```

#### Parameters

*FirstConstraint*
:   First constraint as defined in [swRefPlaneReferenceConstraints\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)

*FirstConstraintAngleOrDistance*
:   Angle or distance of the first constraint

*SecondConstraint*
:   Second constraint as defined in [swRefPlaneReferenceConstraints\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)

*SecondConstraintAngleOrDistance*
:   Angle or distance of the second constraint

*ThirdConstraint*
:   Third constraint as defined in [swRefPlaneReferenceConstraints\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)

*ThirdConstraintAngleOrDistance*
:   Angle or distance of the third constraint

#### Return Value

[Reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

Before calling this method, you must have selected the reference entities using these marks with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md):

- 0 = First reference entity
- 1 = Second reference entity
- 2 = Third reference entity

Example

[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)  
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)  
[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)  
[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)  
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)  
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)
