# ExcludeFromBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ExcludeFromBOM`

Obsolete. Superseded by IComponent2::GetExcludeFromBOM2 and IComponent2::SetExcludeFromBOM2.
Obsolete. Superseded by [IComponent2::GetExcludeFromBOM2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.md) and [IComponent2::SetExcludeFromBOM2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeFromBOM As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
instance.ExcludeFromBOM = value
 
value = instance.ExcludeFromBOM
```

```

System.bool ExcludeFromBOM {get; set;}
```

```

property System.bool ExcludeFromBOM {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude this component from the BOM, false to include it

Remarks

This property applies to [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md); it does not apply to Microsoft Excel-based bills of materials.

If you change this property to true, the name of the component in the FeatureManager design tree changes; (Excluded from BOM) is appended. To update the FeatureManager design tree, call [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.md)
