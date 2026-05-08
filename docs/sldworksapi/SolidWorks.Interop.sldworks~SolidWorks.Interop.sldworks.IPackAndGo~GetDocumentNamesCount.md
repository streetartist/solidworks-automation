# GetDocumentNamesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount`

Gets the number of documents comprising the model for Pack and Go.
Gets the number of documents comprising the model for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentNamesCount() As System.Integer
```

```

Dim instance As IPackAndGo
Dim value As System.Integer
 
value = instance.GetDocumentNamesCount()
```

```

System.int GetDocumentNamesCount()
```

```

System.int GetDocumentNamesCount(); 
```

#### Return Value

Number of documents comprising the model

Remarks

Call this method before calling [IPackAndGo::IGetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.md) and [IPackAndGo::IGetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.md) to determine the size of the array for each method.

Example

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)
