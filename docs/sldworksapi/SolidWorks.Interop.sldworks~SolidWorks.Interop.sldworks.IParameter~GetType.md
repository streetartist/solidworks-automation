# GetType Method (IParameter)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetType`

Gets the type of data stored on the parameter.
Gets the type of data stored on the parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetType() As System.Integer
```

```

Dim instance As IParameter
Dim value As System.Integer
 
value = instance.GetType()
```

```

System.int GetType()
```

```

System.int GetType(); 
```

#### Return Value

Type of data stored on the parameter as defined in [swParam\_Type\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParamType_e.html)

Example

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)  
[Get Document Information (VBA)](Get_Document_Information_Example_VB.htm)  
[Create Note (VBA)](Create_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)
