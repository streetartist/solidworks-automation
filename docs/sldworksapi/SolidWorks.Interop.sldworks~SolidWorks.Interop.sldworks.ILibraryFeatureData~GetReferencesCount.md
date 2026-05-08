# GetReferencesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount`

Gets the number of references for the library feature.
Gets the number of references for the library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencesCount() As System.Integer
```

```

Dim instance As ILibraryFeatureData
Dim value As System.Integer
 
value = instance.GetReferencesCount()
```

```

System.int GetReferencesCount()
```

```

System.int GetReferencesCount(); 
```

#### Return Value

Number of references

Remarks

Call this method before calling [ILibraryFeatureData::IGetReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.md).

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)  
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)  
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.md)  
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.md)  
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.md)
