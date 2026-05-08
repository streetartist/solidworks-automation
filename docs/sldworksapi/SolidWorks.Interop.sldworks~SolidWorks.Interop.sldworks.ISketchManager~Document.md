# Document Property (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Document`

Gets the document for this ISketchManager object.
Gets the document for this [ISketchManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Document As ModelDoc2
```

```

Dim instance As ISketchManager
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

[Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
