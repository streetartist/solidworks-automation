# InsertRib2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRib2`

Obsolete. Superseded by IFeatureManager::InsertRib.
Obsolete. Superseded by [IFeatureManager::InsertRib](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRib.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRib2( _
   ByVal Is2Sided As System.Boolean, _
   ByVal ReverseThicknessDir As System.Boolean, _
   ByVal Thickness As System.Double, _
   ByVal ReferenceEdgeIndex As System.Integer, _
   ByVal ReverseMaterialDir As System.Boolean, _
   ByVal IsDrafted As System.Boolean, _
   ByVal DraftOutward As System.Boolean, _
   ByVal DraftAngle As System.Double, _
   ByVal IsNormToSketch As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Is2Sided As System.Boolean
Dim ReverseThicknessDir As System.Boolean
Dim Thickness As System.Double
Dim ReferenceEdgeIndex As System.Integer
Dim ReverseMaterialDir As System.Boolean
Dim IsDrafted As System.Boolean
Dim DraftOutward As System.Boolean
Dim DraftAngle As System.Double
Dim IsNormToSketch As System.Boolean
 
instance.InsertRib2(Is2Sided, ReverseThicknessDir, Thickness, ReferenceEdgeIndex, ReverseMaterialDir, IsDrafted, DraftOutward, DraftAngle, IsNormToSketch)
```

```

void InsertRib2( 
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle,
   System.bool IsNormToSketch
)
```

```

void InsertRib2( 
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle,
   System.bool IsNormToSketch
) 
```

#### Parameters

*Is2Sided*
:   True if the rib is double-sided rib, false if the rib is single sided; a double-sided rib thickens on both sides of the sketch

*ReverseThicknessDir*
:   For single-sided ribs, the direction thickened is the opposite side of the sketch normal

*Thickness*
:   Rib thickness

*ReferenceEdgeIndex*
:   Edge in the sketch to us to determine the material direction and for draft reference; when the rib is drafted, the mid point of this edge maintains the thickness value; other points on the rib may have a different thickness due to the draft

*ReverseMaterialDir*
:   Which direction the rib has material; it is on one side or the order side of the reference edge base on this flag

*IsDrafted*
:   True if the rib is drafted, false if not

*DraftOutward*
:   True to draft outwards, false to not

*DraftAngle*
:   Draft angle to apply to the rib

*IsNormToSketch*
:   True if the rib is normal to the sketch, false if the rib is parallel to the sketch

Remarks

This method supports multibody parts. You must select the input body by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and setting its Mark argument to 1 before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
