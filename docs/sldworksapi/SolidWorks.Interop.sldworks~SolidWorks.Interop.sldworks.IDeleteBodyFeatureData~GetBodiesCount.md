# GetBodiesCount Method (IDeleteBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount`

Gets the number of bodies to delete or keep.
Gets the number of bodies to delete or keep.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesCount() As System.Integer
```

```

Dim instance As IDeleteBodyFeatureData
Dim value As System.Integer
 
value = instance.GetBodiesCount()
```

```

System.int GetBodiesCount()
```

```

System.int GetBodiesCount(); 
```

#### Return Value

Number of bodies

Remarks

Call this method before calling [IDeleteBodyFeautre::IGetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.md) to determine the size of the array.

Example

See the [IDeleteBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md)  
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.md)  
[IDeleteBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.md)  
[IDeleteBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.md)
