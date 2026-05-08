# DAssemblyDocEvents_DeleteItemPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemPreNotifyEventHandler`

Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).
Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_DeleteItemPreNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_DeleteItemPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_DeleteItemPreNotifyEventHandler( 
   System.int EntityType,
   System.string itemName
)
```

```

public delegate System.int DAssemblyDocEvents_DeleteItemPreNotifyEventHandler( 
   System.int EntityType,
   System.String^ itemName
)
```

#### Parameters

*EntityType*
:   Type of entity to delete as defined in [swNotifyEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)

*itemName*
:   Name of the entity to delete

Remarks

If developing a C++ application, use [swAssemblyDeleteSelectionPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [IAssemblyDoc::FeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName.md) or [IAssemblyDoc::IFeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.md) or [IModelDoc2::GetConfigurationByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.md) and [IModelDoc2::IGetConfigurationByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.md) to get the object being deleted. Use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_DeleteItemPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
