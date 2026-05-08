# InsertFilletBeadFeature3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature3`

Inserts fillet weld bead features for the specified face sets.
Inserts fillet weld bead features for the specified face sets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFilletBeadFeature3( _
   ByVal Type1 As System.Short, _
   ByVal Size1 As System.Double, _
   ByVal Length1 As System.Double, _
   ByVal PenetrationType1 As System.Short, _
   ByVal PenetrationValue1 As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Type2 As System.Short, _
   ByVal Size2 As System.Double, _
   ByVal Length2 As System.Double, _
   ByVal PenetrationType2 As System.Short, _
   ByVal PenetrationValue2 As System.Double, _
   ByVal Flag As System.Integer, _
   ByVal EdgeNum1 As System.Integer, _
   ByVal DeSelEdge1 As System.Object, _
   ByVal EdgeNum2 As System.Integer, _
   ByVal DeSelEdge2 As System.Object, _
   ByVal FaceSet1 As System.Object, _
   ByVal FaceSet2 As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type1 As System.Short
Dim Size1 As System.Double
Dim Length1 As System.Double
Dim PenetrationType1 As System.Short
Dim PenetrationValue1 As System.Double
Dim Pitch As System.Double
Dim Type2 As System.Short
Dim Size2 As System.Double
Dim Length2 As System.Double
Dim PenetrationType2 As System.Short
Dim PenetrationValue2 As System.Double
Dim Flag As System.Integer
Dim EdgeNum1 As System.Integer
Dim DeSelEdge1 As System.Object
Dim EdgeNum2 As System.Integer
Dim DeSelEdge2 As System.Object
Dim FaceSet1 As System.Object
Dim FaceSet2 As System.Object
Dim value As Feature
 
value = instance.InsertFilletBeadFeature3(Type1, Size1, Length1, PenetrationType1, PenetrationValue1, Pitch, Type2, Size2, Length2, PenetrationType2, PenetrationValue2, Flag, EdgeNum1, DeSelEdge1, EdgeNum2, DeSelEdge2, FaceSet1, FaceSet2)
```

```

Feature InsertFilletBeadFeature3( 
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.short PenetrationType1,
   System.double PenetrationValue1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
   System.short PenetrationType2,
   System.double PenetrationValue2,
   System.int Flag,
   System.int EdgeNum1,
   System.object DeSelEdge1,
   System.int EdgeNum2,
   System.object DeSelEdge2,
   System.object FaceSet1,
   System.object FaceSet2
)
```

```

Feature^ InsertFilletBeadFeature3( 
   System.short Type1,
   System.double Size1,
   System.double Length1,
   System.short PenetrationType1,
   System.double PenetrationValue1,
   System.double Pitch,
   System.short Type2,
   System.double Size2,
   System.double Length2,
   System.short PenetrationType2,
   System.double PenetrationValue2,
   System.int Flag,
   System.int EdgeNum1,
   System.Object^ DeSelEdge1,
   System.int EdgeNum2,
   System.Object^ DeSelEdge2,
   System.Object^ FaceSet1,
   System.Object^ FaceSet2
) 
```

#### Parameters

*Type1*
:   First side:

    - 0 = Full length
    - 1 = Intermittent
    - 2 = Staggered

*Size1*
:   Size of fillet on first side

*Length1*
:   Length of fillet on first side

*PenetrationType1*
:   First side:

    - 0 = Full penetration
    - 1 = Partial penetration
    - 2 = No penetration

*PenetrationValue1*
:   If penetrationType1 is set to 1 (Partial penetration), then set its value

*Pitch*
:   Pitch, if Intermittent or Staggered on both sides

*Type2*
:   Second side:

    - 0= Full length
    - 1 = Intermittent
    - 2= Staggered

*Size2*
:   Size of fillet on second side

*Length2*
:   Length of fillet on second side

*PenetrationType2*
:   Second side:

    - 0 = Full penetration
    - 1 = Partial penetration
    - 2 = No penetration

*PenetrationValue2*
:   If penetrationType2 is set to 1 (Partial penetration), then set its value

*Flag*
:   - 0 = One-sided and no tangent propagation
    - 1 = Two-sided
    - 2 = Tangent propagation
    - 3 = Two-sided and tangent propagation

*EdgeNum1*
:   Number of intersecting edges on first side

*DeSelEdge1*
:   Array indicating if intersecting edges are selected (0) or deselected (1) on first side

*EdgeNum2*
:   Number of intersecting edges on second side

*DeSelEdge2*
:   Array indicating if intersecting edges are selected (0) or deselected (1) on second side

*FaceSet1*
:   Array of side 1 [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) whose intersecting edges get fillet beads

*FaceSet2*
:   Array of side 2 [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) whose intersecting edges get fillet beads

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This interface specifies two face arrays, one for each side of a part feature. The fillet bead is applied to the edges where each face intersects for each array specified.

Example

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)  
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)  
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IFeatureManager::InsertFilletBeadFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature2.md)
