# SetDraftWhileExtruding Method (IExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetDraftWhileExtruding`

Obsolete. Superseded by IExtrudeFeatureData2::SetDraftWhileExtruding.
Obsolete. Superseded by [IExtrudeFeatureData2::SetDraftWhileExtruding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDraftWhileExtruding( _
   ByVal Forward As System.Boolean, _
   ByVal DraftWhileExtrude As System.Boolean _
) 
```

```

Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim DraftWhileExtrude As System.Boolean
 
instance.SetDraftWhileExtruding(Forward, DraftWhileExtrude)
```

```

void SetDraftWhileExtruding( 
   System.bool Forward,
   System.bool DraftWhileExtrude
)
```

```

void SetDraftWhileExtruding( 
   System.bool Forward,
   System.bool DraftWhileExtrude
) 
```

#### Parameters

*Forward*

*DraftWhileExtrude*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.md)  
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.md)
