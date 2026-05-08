# RepairMissingReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RepairMissingReferences`

Finds missing references in this fillet/chamfer and reassigns them to new edges.
Finds missing references in this fillet/chamfer and reassigns them to new edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RepairMissingReferences() 
```

```

Dim instance As ISimpleFilletFeatureData2
 
instance.RepairMissingReferences()
```

```

void RepairMissingReferences()
```

```

void RepairMissingReferences(); 
```

Remarks

If you delete a feature that this fillet or chamfer is referencing and then create a similar feature with the same geometry, the references do not reattach. The missing references appear in the **Items To Fillet** list box of the Fillet PropertyManager, but finding the valid edges to reattach is difficult. Call this method to find all missing references and reassign them to new edges.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
