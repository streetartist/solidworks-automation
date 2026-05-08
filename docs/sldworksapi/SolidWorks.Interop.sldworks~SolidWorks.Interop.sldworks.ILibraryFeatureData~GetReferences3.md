# GetReferences3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences3`

Gets the references with respect to the specified scope.
Gets the references with respect to the specified scope.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferences3( _
   ByVal Scope As System.Integer, _
   ByRef RefType As System.Object, _
   ByRef RefName As System.Object _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim RefType As System.Object
Dim RefName As System.Object
Dim value As System.Object
 
value = instance.GetReferences3(Scope, RefType, RefName)
```

```

System.object GetReferences3( 
   System.int Scope,
   out System.object RefType,
   out System.object RefName
)
```

```

System.Object^ GetReferences3( 
   System.int Scope,
   [Out] System.Object^ RefType,
   [Out] System.Object^ RefName
) 
```

#### Parameters

*Scope*
:   Reference scope as defined in [swLibFeatureData\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)

*RefType*
:   Array of reference types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*RefName*
:   Array of reference names

#### Return Value

Array of references

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

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
[ILibraryFeatureData::SetReferences Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.md)  
[ILibraryFeatureData::ISetReferences Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.md)  
[ILibraryFeatureData::IGetReferences3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences3.md)
