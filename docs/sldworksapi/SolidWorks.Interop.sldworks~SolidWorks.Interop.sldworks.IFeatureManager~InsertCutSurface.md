# InsertCutSurface Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSurface`

Inserts a surface-cut feature using the preselected surface or plane.
Inserts a surface-cut feature using the preselected surface or plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCutSurface( _
   ByVal Flip As System.Boolean, _
   ByVal KeepPieceIndex As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal Bodies As System.Object, _
   ByRef Error As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Flip As System.Boolean
Dim KeepPieceIndex As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim Bodies As System.Object
Dim Error As System.Integer
Dim value As Feature
 
value = instance.InsertCutSurface(Flip, KeepPieceIndex, UseFeatScope, UseAutoSelect, Bodies, Error)
```

```

Feature InsertCutSurface( 
   System.bool Flip,
   System.int KeepPieceIndex,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.object Bodies,
   out System.int Error
)
```

```

Feature^ InsertCutSurface( 
   System.bool Flip,
   System.int KeepPieceIndex,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.Object^ Bodies,
   [Out] System.int Error
) 
```

#### Parameters

*Flip*
:   True to flip the direction of the cut, false to not

*KeepPieceIndex*
:   Piece to keep if there is ambiguity (see **Remarks**)

*UseFeatScope*
:   True to cut only the bodies passed to Bodies that intersect with the cut, false to cut all bodies that intersect with the cut

*UseAutoSelect*
:   True to automatically cut all bodies that intersect with the cut, false to cut only the bodies passed to Bodies that intersect with the cut

*Bodies*
:   - Array of specific [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that intersect with the cut
      - UseFeatScope = true
      - UseAutoSelect = false

    - or -

    - Empty array indicating to cut all bodies that intersect with the cut
      - UseFeatScope = false
      - UseAutoSelect = true

*Error*
:   Status of the cut as defined in [swSurfaceCutFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceCutFeatureError_e.html)

#### Return Value

Surface-cut [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

When there is ambiguity in the result of a cut, KeepPieceIndex is used to resolve which of the possible results is used. This can be set to -1 if there is no ambiguity; otherwise, it should be the index of the result, starting from 0 (up to one less than the possible number of outcomes).

Example

[Insert Surface-cut Feature (C#)](Insert_Surface-cut_Feature_Example_CSharp.htm)  
[Insert Surface-cut Feature (VB.NET)](Insert_Surface-cut_Feature_Example_VBNET.htm)  
[Insert Surface-cut Feature (VBA)](Insert_Surface-cut_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)
