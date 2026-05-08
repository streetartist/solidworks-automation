# GetEntityParamsSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~GetEntityParamsSize`

Gets the number of parameters for this mate entity.
Gets the number of parameters for this mate entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntityParamsSize() As System.Integer
```

```

Dim instance As IMateEntity2
Dim value As System.Integer
 
value = instance.GetEntityParamsSize()
```

```

System.int GetEntityParamsSize()
```

```

System.int GetEntityParamsSize(); 
```

#### Return Value

Number of parameters for this mate entity

Remarks

Call this method before calling [IMateEntity2::IGetEntityParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~IGetEntityParams.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)  
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.md)  
[IMateEntity2::EntityParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~EntityParams.md)
