# InsertMfDraft Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertMfDraft`

Obsolete. Superseded by IModelDoc2::InsertMfDraft.
Obsolete. Superseded by [IModelDoc2::InsertMfDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMfDraft.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertMfDraft( _
   ByVal Angle As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal IsEdgeDraft As System.Boolean, _
   ByVal PropType As System.Integer _
) 
```

```

Dim instance As IModelDoc
Dim Angle As System.Double
Dim FlipDir As System.Boolean
Dim IsEdgeDraft As System.Boolean
Dim PropType As System.Integer
 
instance.InsertMfDraft(Angle, FlipDir, IsEdgeDraft, PropType)
```

```

void InsertMfDraft( 
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType
)
```

```

void InsertMfDraft( 
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType
) 
```

#### Parameters

*Angle*

*FlipDir*

*IsEdgeDraft*

*PropType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
