# ModelDoc Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~ModelDoc`

Gets the model document in this model window.
Gets the model document in this model window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ModelDoc As ModelDoc2
```

```

Dim instance As IModelWindow
Dim value As ModelDoc2
 
value = instance.ModelDoc
```

```

ModelDoc2 ModelDoc {get;}
```

```

property ModelDoc2^ ModelDoc {
   ModelDoc2^ get();
}
```

#### Property Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in this model window

Example

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)  
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)  
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)  
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.md)
