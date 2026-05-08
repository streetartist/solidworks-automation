# GetJoinedPartsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount`

Gets the number of joined parts.
Gets the number of joined parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetJoinedPartsCount() As System.Integer
```

```

Dim instance As IJoinFeatureData
Dim value As System.Integer
 
value = instance.GetJoinedPartsCount()
```

```

System.int GetJoinedPartsCount()
```

```

System.int GetJoinedPartsCount(); 
```

#### Return Value

Number of joined parts

Remarks

Call this method before calling [IJoinFeatureData::IGetJoinedParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.md) to determine the size of the array.

Example

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)  
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)  
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)  
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.md)  
[IJoinFeatureData::ISetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.md)  
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.md)
