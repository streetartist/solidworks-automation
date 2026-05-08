# InsertRib Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertRib`

Obsolete. Superseded by IModelDoc2::InsertRib.
Obsolete. Superseded by [IModelDoc2::InsertRib](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRib.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRib( _
   ByVal Is2Sided As System.Boolean, _
   ByVal ReverseThicknessDir As System.Boolean, _
   ByVal Thickness As System.Double, _
   ByVal ReferenceEdgeIndex As System.Integer, _
   ByVal ReverseMaterialDir As System.Boolean, _
   ByVal IsDrafted As System.Boolean, _
   ByVal DraftOutward As System.Boolean, _
   ByVal DraftAngle As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim Is2Sided As System.Boolean
Dim ReverseThicknessDir As System.Boolean
Dim Thickness As System.Double
Dim ReferenceEdgeIndex As System.Integer
Dim ReverseMaterialDir As System.Boolean
Dim IsDrafted As System.Boolean
Dim DraftOutward As System.Boolean
Dim DraftAngle As System.Double
 
instance.InsertRib(Is2Sided, ReverseThicknessDir, Thickness, ReferenceEdgeIndex, ReverseMaterialDir, IsDrafted, DraftOutward, DraftAngle)
```

```

void InsertRib( 
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle
)
```

```

void InsertRib( 
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle
) 
```

#### Parameters

*Is2Sided*

*ReverseThicknessDir*

*Thickness*

*ReferenceEdgeIndex*

*ReverseMaterialDir*

*IsDrafted*

*DraftOutward*

*DraftAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
