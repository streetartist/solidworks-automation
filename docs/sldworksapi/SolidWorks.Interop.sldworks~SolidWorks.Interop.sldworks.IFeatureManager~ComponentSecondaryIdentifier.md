# ComponentSecondaryIdentifier Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentSecondaryIdentifier`

Gets the secondary element(s) displayed for the components in the FeatureManager design tree.
Gets the secondary element(s) displayed for the components in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ComponentSecondaryIdentifier As System.Integer
```

```

Dim instance As IFeatureManager
Dim value As System.Integer
 
value = instance.ComponentSecondaryIdentifier
```

```

System.int ComponentSecondaryIdentifier {get;}
```

```

property System.int ComponentSecondaryIdentifier {
   System.int get();
}
```

#### Property Value

Secondary identifier(s) as defined by [swComponentIdentifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html)

Remarks

This property works in both SOLIDWORKS Desktop and [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::SetComponentIdentifiers Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.md)
