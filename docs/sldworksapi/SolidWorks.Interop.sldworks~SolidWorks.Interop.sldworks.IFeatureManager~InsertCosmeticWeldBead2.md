# InsertCosmeticWeldBead2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2`

Inserts a cosmetic weld bead using either weld geometry or a weld path.
Inserts a cosmetic weld bead using either weld geometry or a weld path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCosmeticWeldBead2( _
   ByVal WeldMode As System.Integer, _
   ByVal WeldFromFaceOrEdgeSet As System.Object, _
   ByVal WeldToFaceOrEdgeSet As System.Object, _
   ByVal WeldSize As System.Double _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim WeldMode As System.Integer
Dim WeldFromFaceOrEdgeSet As System.Object
Dim WeldToFaceOrEdgeSet As System.Object
Dim WeldSize As System.Double
Dim value As System.Object
 
value = instance.InsertCosmeticWeldBead2(WeldMode, WeldFromFaceOrEdgeSet, WeldToFaceOrEdgeSet, WeldSize)
```

```

System.object InsertCosmeticWeldBead2( 
   System.int WeldMode,
   System.object WeldFromFaceOrEdgeSet,
   System.object WeldToFaceOrEdgeSet,
   System.double WeldSize
)
```

```

System.Object^ InsertCosmeticWeldBead2( 
   System.int WeldMode,
   System.Object^ WeldFromFaceOrEdgeSet,
   System.Object^ WeldToFaceOrEdgeSet,
   System.double WeldSize
) 
```

#### Parameters

*WeldMode*
:   Weld mode as defined in[swCosmeticWeldBeadMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCosmeticWeldBeadMode_e.html)

*WeldFromFaceOrEdgeSet*
:   Array of weld-from entities (see **Remarks**)

*WeldToFaceOrEdgeSet*
:   Array of weld-to entities or Nothing or null (see **Remarks**)

*WeldSize*
:   Size of weld bead

#### Return Value

Array of weld bead [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

|  |  |  |
| --- | --- | --- |
| **WeldMode** | **Selected entities** | **Selection marks** |
| swCosmeticWeldBeadMode\_e.swCosmeticWeldBeadMode\_WeldGeometry | Either [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) as weld-from and weld-to entities    **NOTE**: Both weld-to and weld-from entities must all be the same type of entities; e.g., all faces or all edges. | - 4 for each weld-from entity in WeldFromFaceOrEdgeSet  - 8 for each weld-to entity in WeldToFaceOrEdgeSet |
| swCosmeticWeldBeadMode\_e.swCosmeticWeldBeadMode\_WeldPath | Edges, [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), or a combination of edges and sketches are selected as weld-from entities | - 0 for each weld-from entity in WeldFromFaceOrEdgeSet - Nothing or null for WeldToFaceOrEdgeSet |

Example

[Insert Cosmetic Weld Bead Using Geometric Entities (C#)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_CSharp.htm)  
[Insert Cosmetic Weld Bead Using Geometric Entities (VB.NET)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VBNET.htm)  
[Insert Cosmetic Weld Bead Using Geometric Entities (VBA)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
