# InsertMfDraft2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertMfDraft2`

Obsolete. Superseded by IModelDoc2::InsertMfDraft2.
Obsolete. Superseded by [IModelDoc2::InsertMfDraft2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMfDraft2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertMfDraft2( _
   ByVal Angle As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal IsEdgeDraft As System.Boolean, _
   ByVal PropType As System.Integer, _
   ByVal StepDraft As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim Angle As System.Double
Dim FlipDir As System.Boolean
Dim IsEdgeDraft As System.Boolean
Dim PropType As System.Integer
Dim StepDraft As System.Boolean
 
instance.InsertMfDraft2(Angle, FlipDir, IsEdgeDraft, PropType, StepDraft)
```

```

void InsertMfDraft2( 
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType,
   System.bool StepDraft
)
```

```

void InsertMfDraft2( 
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType,
   System.bool StepDraft
) 
```

#### Parameters

*Angle*

*FlipDir*

*IsEdgeDraft*

*PropType*

*StepDraft*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
