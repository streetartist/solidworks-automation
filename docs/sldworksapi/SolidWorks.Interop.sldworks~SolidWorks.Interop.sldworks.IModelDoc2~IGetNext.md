# IGetNext Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNext`

Gets the next document in the current SOLIDWORKS session.
Gets the next document in the current SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNext() As ModelDoc2
```

```

Dim instance As IModelDoc2
Dim value As ModelDoc2
 
value = instance.IGetNext()
```

```

ModelDoc2 IGetNext()
```

```

ModelDoc2^ IGetNext(); 
```

#### Return Value

Next [model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in the current SOLIDWORKS session

Remarks

To traverse all documents open in this SOLIDWORKS session, the first IModleDoc2 object that calls this method must have been returned from [ISldWorks::IGetFirstDocument2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md).

**NOTE:** This method is available in datecode 1999/207 and later.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNext.md)
