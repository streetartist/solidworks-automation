# InsertCutSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCutSurface`

Obsolete. Superseded by IFeatureManager::InsertCutSurface.
Obsolete. Superseded by [IFeatureManager::InsertCutSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertCutSurface( _
   ByVal Flip As System.Boolean, _
   ByVal KeepPieceIndex As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Flip As System.Boolean
Dim KeepPieceIndex As System.Integer
 
instance.InsertCutSurface(Flip, KeepPieceIndex)
```

```

void InsertCutSurface( 
   System.bool Flip,
   System.int KeepPieceIndex
)
```

```

void InsertCutSurface( 
   System.bool Flip,
   System.int KeepPieceIndex
) 
```

#### Parameters

*Flip*
:   True to flip the direction, false to not

*KeepPieceIndex*
:   Piece to keep if there is ambiguity

Remarks

When there is ambiguity in the result of a cut, KeepPieceIndex is used to resolve which of the possible results is used. This can be set to -1 if there is no ambiguity; otherwise, it should be the index of the result, starting from 0 (up to one less than the possible number of outcomes).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)
