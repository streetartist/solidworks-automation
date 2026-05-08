# GetReferences2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences2`

Obsolete. Superseded by ILibraryFeatureData::GetReferences3.
Obsolete. Superseded by [ILibraryFeatureData::GetReferences3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferences2( _
   ByVal Scope As System.Integer, _
   ByRef RefType As System.Object _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim RefType As System.Object
Dim value As System.Object
 
value = instance.GetReferences2(Scope, RefType)
```

```

System.object GetReferences2( 
   System.int Scope,
   out System.object RefType
)
```

```

System.Object^ GetReferences2( 
   System.int Scope,
   [Out] System.Object^ RefType
) 
```

#### Parameters

*Scope*
:   Reference scope as defined in [swLibFeatureData\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)

*RefType*
:   Array of reference types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Array of references

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::IGetReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences2.md)  
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.md)  
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.md)
