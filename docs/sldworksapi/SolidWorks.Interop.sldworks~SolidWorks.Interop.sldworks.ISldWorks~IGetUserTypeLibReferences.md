# IGetUserTypeLibReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences`

Gets the specified user-specified type library references.
Gets the specified user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUserTypeLibReferences( _
   ByVal NCount As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim NCount As System.Integer
Dim value As System.String
 
value = instance.IGetUserTypeLibReferences(NCount)
```

```

System.string IGetUserTypeLibReferences( 
   System.int NCount
)
```

```

System.String^ IGetUserTypeLibReferences( 
   System.int NCount
) 
```

#### Parameters

*NCount*
:   Number of user-specified type libraries

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings for the user-specified type library references.

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISldWorks::GetUserTypeLibReferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.md) to get the value for NCount.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.md)  
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.md)  
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.md)  
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.md)
