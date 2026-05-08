# EnumFaces Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces`

Returns an enumerated list of the faces in a body.
Returns an enumerated list of the faces in a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumFaces() As EnumFaces2
```

```

Dim instance As IBody2
Dim value As EnumFaces2
 
value = instance.EnumFaces()
```

```

EnumFaces2 EnumFaces()
```

```

EnumFaces2^ EnumFaces(); 
```

#### Return Value

Enumerated list of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) (see **Remarks**)

Remarks

OLE automation applications should use [IBody2::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetNextFace.md) and [IFace2::GetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.md).

Example

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
