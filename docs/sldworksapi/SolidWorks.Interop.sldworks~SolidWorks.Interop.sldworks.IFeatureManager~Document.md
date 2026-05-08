# Document Property (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~Document`

Gets the specified document.
Gets the specified document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Document As ModelDoc2
```

```

Dim instance As IFeatureManager
Dim value As ModelDoc2
 
value = instance.Document
```

```

ModelDoc2 Document {get;}
```

```

property ModelDoc2^ Document {
   ModelDoc2^ get();
}
```

#### Property Value

[Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) to get

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IModelDocExtension::Document Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Document.md)  
[IModelViewManager::Document Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~Document.md)
