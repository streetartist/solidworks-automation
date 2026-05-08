# AccessBeltPart Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~AccessBeltPart`

Gets the belt part.
Gets the belt part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessBeltPart() As PartDoc
```

```

Dim instance As IBeltChainFeatureData
Dim value As PartDoc
 
value = instance.AccessBeltPart()
```

```

PartDoc AccessBeltPart()
```

```

PartDoc^ AccessBeltPart(); 
```

#### Return Value

[IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)

Remarks

This method is valid only if [IBeltChainFeatureData::CreateBeltPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~CreateBeltPart.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
