# ViewFeatureManagerFeatureDetail Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerFeatureDetail`

Obsolete. Superseded by IFeatureManager::ShowFeatureDetails.
Obsolete. Superseded by [IFeatureManager::ShowFeatureDetails](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ViewFeatureManagerFeatureDetail( _
   ByVal Detail As System.Boolean _
) 
```

```

Dim instance As IAssemblyDoc
Dim Detail As System.Boolean
 
instance.ViewFeatureManagerFeatureDetail(Detail)
```

```

void ViewFeatureManagerFeatureDetail( 
   System.bool Detail
)
```

```

void ViewFeatureManagerFeatureDetail( 
   System.bool Detail
) 
```

#### Parameters

*Detail*
:   True to show feature detail, false to hide it

Remarks

This method affects the FeatureManager design tree view of the current configuration of the assembly. It does not affect other configurations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ViewFeatureManagerByDependencies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerByDependencies.md)  
[IAssemblyDoc::ViewFeatureManagerByFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerByFeatures.md)
