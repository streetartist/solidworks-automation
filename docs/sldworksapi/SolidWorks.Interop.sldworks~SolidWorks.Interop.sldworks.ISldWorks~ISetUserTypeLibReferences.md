# ISetUserTypeLibReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences`

Sets the user-specified type library references.
Sets the user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetUserTypeLibReferences( _
   ByVal NCount As System.Integer, _
   ByRef BstrTlbRef As System.String _
) 
```

```

Dim instance As ISldWorks
Dim NCount As System.Integer
Dim BstrTlbRef As System.String
 
instance.ISetUserTypeLibReferences(NCount, BstrTlbRef)
```

```

void ISetUserTypeLibReferences( 
   System.int NCount,
   ref System.string BstrTlbRef
)
```

```

void ISetUserTypeLibReferences( 
   System.int NCount,
   System.String^% BstrTlbRef
) 
```

#### Parameters

*NCount*
:   Number of user-specified type library references

*BstrTlbRef*
:   - in-process, unmanaged C++: Pointer to an array of strings of the user-specified type library references

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

- An add-in can use this method to add its type library references after the add-in is loaded.
- A user-specified type library first appears on the list of available references only after adding it and only after recording a macro.
- User-specified type library references are not persistent across SOLIDWORKS sessions.
- Only macros created after adding a user-specified type library reference can reference that type library.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetUserTypeLibReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.md)  
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.md)  
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.md)  
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.md)  
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.md)
