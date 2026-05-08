# IGetReferences3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences3`

Gets the references with respect to the specified scope.
Gets the references with respect to the specified scope.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetReferences3( _
   ByVal Scope As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef RefType As System.Integer, _
   ByRef RefName As System.String _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim Count As System.Integer
Dim RefType As System.Integer
Dim RefName As System.String
Dim value As System.Object
 
value = instance.IGetReferences3(Scope, Count, RefType, RefName)
```

```

System.object IGetReferences3( 
   System.int Scope,
   System.int Count,
   out System.int RefType,
   out System.string RefName
)
```

```

System.Object^ IGetReferences3( 
   System.int Scope,
   System.int Count,
   [Out] System.int RefType,
   [Out] System.String^ RefName
) 
```

#### Parameters

*Scope*
:   Reference scope as defined in [swLibFeatureData\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)

*Count*
:   Number of references

*RefType*
:   - In-process, unmanaged C++: Pointer to an array of type long of reference types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*RefName*
:   - In-process, unmanaged C++: Pointer to an array of reference names
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- In-process, unmanaged C++: Pointer to an array of references

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ILibraryFeatureData::GetReferencesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.md) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetReferences3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences3.md)
