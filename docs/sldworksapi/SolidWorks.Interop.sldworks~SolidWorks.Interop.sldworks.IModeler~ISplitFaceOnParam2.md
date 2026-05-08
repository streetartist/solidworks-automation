# ISplitFaceOnParam2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2`

Splits and retrieves the faces on the U or V parameter.
Splits and retrieves the faces on the U or V parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISplitFaceOnParam2() As Face2
```

```

Dim instance As IModeler
Dim value As Face2
 
value = instance.ISplitFaceOnParam2()
```

```

Face2 ISplitFaceOnParam2()
```

```

Face2^ ISplitFaceOnParam2(); 
```

#### Return Value

Array of new [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

The split is defined by calling [IModeler::ISplitFaceOnParamCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.md). Then call this method to retrieve the list of new faces allocated.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::SplitFaceOnParam Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.md)
