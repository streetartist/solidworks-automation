# FeatureExtruRefSurface3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtruRefSurface3`

Inserts an extruded surface.
Inserts an extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureExtruRefSurface3( _
   ByVal Sd As System.Boolean, _
   ByVal Dir As System.Boolean, _
   ByVal StartCond As System.Integer, _
   ByVal OffsetVal As System.Double, _
   ByVal T1 As System.Integer, _
   ByVal T2 As System.Integer, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal Dchk1 As System.Boolean, _
   ByVal Dchk2 As System.Boolean, _
   ByVal Ddir1 As System.Boolean, _
   ByVal Ddir2 As System.Boolean, _
   ByVal Dang1 As System.Double, _
   ByVal Dang2 As System.Double, _
   ByVal OffsetReverse1 As System.Boolean, _
   ByVal OffsetReverse2 As System.Boolean, _
   ByVal TranslateSurface1 As System.Boolean, _
   ByVal TranslateSurface2 As System.Boolean, _
   ByVal CapEnd1 As System.Boolean, _
   ByVal CapEnd2 As System.Boolean, _
   ByVal DeleteOriginalFace As System.Boolean, _
   ByVal KnitResult As System.Boolean _
) 
```

```

Dim instance As IFeatureManager
Dim Sd As System.Boolean
Dim Dir As System.Boolean
Dim StartCond As System.Integer
Dim OffsetVal As System.Double
Dim T1 As System.Integer
Dim T2 As System.Integer
Dim D1 As System.Double
Dim D2 As System.Double
Dim Dchk1 As System.Boolean
Dim Dchk2 As System.Boolean
Dim Ddir1 As System.Boolean
Dim Ddir2 As System.Boolean
Dim Dang1 As System.Double
Dim Dang2 As System.Double
Dim OffsetReverse1 As System.Boolean
Dim OffsetReverse2 As System.Boolean
Dim TranslateSurface1 As System.Boolean
Dim TranslateSurface2 As System.Boolean
Dim CapEnd1 As System.Boolean
Dim CapEnd2 As System.Boolean
Dim DeleteOriginalFace As System.Boolean
Dim KnitResult As System.Boolean
 
instance.FeatureExtruRefSurface3(Sd, Dir, StartCond, OffsetVal, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, TranslateSurface1, TranslateSurface2, CapEnd1, CapEnd2, DeleteOriginalFace, KnitResult)
```

```

void FeatureExtruRefSurface3( 
   System.bool Sd,
   System.bool Dir,
   System.int StartCond,
   System.double OffsetVal,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool CapEnd1,
   System.bool CapEnd2,
   System.bool DeleteOriginalFace,
   System.bool KnitResult
)
```

```

void FeatureExtruRefSurface3( 
   System.bool Sd,
   System.bool Dir,
   System.int StartCond,
   System.double OffsetVal,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool CapEnd1,
   System.bool CapEnd2,
   System.bool DeleteOriginalFace,
   System.bool KnitResult
) 
```

#### Parameters

*Sd*
:   True for single-ended, false for double-ended

*Dir*
:   True to reverse the direction of the extrude, false to not

*StartCond*
:   Start condition as defined in [swStartConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStartConditions_e.html)

*OffsetVal*
:   Offset value

*T1*
:   Termination type for first end as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*T2*
:   Termination type for second end as defined in swEndConditions\_e (valid only if Sd = false)

*D1*
:   Depth of extrusion for first end in meters

*D2*
:   Depth of extrusion for second end in meters (valid only if Sd = false)

*Dchk1*
:   True allows draft angle in first direction, false does not allow drafting

*Dchk2*
:   True allows draft angle in second direction, false does not allow drafting (valid only if Sd = false)

*Ddir1*
:   True for first draft angle to be outward, false for first draft angle to be inward

*Ddir2*
:   True for second draft angle to be outward, false for second draft angle to be inward (valid only if Sd = false)

*Dang1*
:   Draft angle for first end

*Dang2*
:   Draft angle for second end (valid only if Sd = false)

*OffsetReverse1*
:   If you choose to offset the first end condition from another face or plane, then true specifies the offset from the face or plane in a direction away from the sketch, and false specifies the offset in a direction toward the sketch

*OffsetReverse2*
:   If you choose to offset the second end condition from another face or plane, then true specifies the offset from the face or plane in a direction away from the sketch, and false specifies the offset in a direction toward the sketch (valid only if Sd = false)

*TranslateSurface1*
:   If you specified T1 as swEndConditions\_e.swEndCondOffsetFromSurface, then true specifies that the end of the extrusion is a translation of the reference surface, and false specifies to use a true offset

*TranslateSurface2*
:   If you specified T2 as swEndConditions\_e.swEndCondOffsetFromSurface, then true specifies that the end of the extrusion is a translation of the reference surface, and false specifies to use a true offset (valid only if Sd = false)

*CapEnd1*
:   True to cap first end, false to not

*CapEnd2*
:   True to cap second end, false to not (valid only if Sd = false)

*DeleteOriginalFace*
:   True to delete original faces, false to not (valid only if Sd = true)

*KnitResult*
:   True to knit the extrusion result, false to not (valid only if Sd = true and DeleteOriginalFace = true)

Remarks

Before calling this method, select the entities for the extruded surface using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

| Entity | Mark |
| --- | --- |
| Base   - 2D or 3D sketch - Sketch segments - Single planar face - Multiple co-planar faces | - 0 - 0 or 4 - 0 - 0 for first planar face and 256 for all other co-planar faces |
| Direction edge | 16 |
| Start condition entity | 32 |
| End condition entity | 1 |

Example

[Insert Extruded Surface (C#)](Insert_Extruded_Reference_Surface_Example_CSharp.htm)  
[Insert Extruded Surface (VB.NET)](Insert_Extruded_Reference_Surface_Example_VBNET.htm)  
[Insert Extruded Surface (VBA)](Insert_Extruded_Reference_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)
