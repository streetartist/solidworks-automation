# GetUpdateStamp Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetUpdateStamp`

Gets the update stamp for the body as of the last rebuild.
Gets the update stamp for the body as of the last rebuild.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUpdateStamp() As System.Integer
```

```

Dim instance As IBody2
Dim value As System.Integer
 
value = instance.GetUpdateStamp()
```

```

System.int GetUpdateStamp()
```

```

System.int GetUpdateStamp(); 
```

#### Return Value

Update stamp

Remarks

The update stamp is not changed if the features contributing to the body geometry have not been rebuilt.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
