# SetDraftWhileExtruding Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding`

Sets whether the feature is drafted while extruding in the forward or reverse direction.
Sets whether the feature is drafted while extruding in the forward or reverse direction.

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

Dim instance As IExtrudeFeatureData2
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
:   True for forward direction, false for reverse

*DraftWhileExtrude*
:   True if the feature is drafted while extruding, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.md)  
[IExtrudeFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.md)  
[IExtrudeFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.md)  
[IExtrudeFeatureData2::SetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.md)  
[IExtrudeFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.md)
