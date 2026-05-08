# IRemoveUserTypeLibReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences`

Removes the user-specified type library references.
Removes the user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRemoveUserTypeLibReferences( _
   ByVal NCount As System.Integer, _
   ByRef BstrTlbRef As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim NCount As System.Integer
Dim BstrTlbRef As System.String
Dim value As System.Boolean
 
value = instance.IRemoveUserTypeLibReferences(NCount, BstrTlbRef)
```

```

System.bool IRemoveUserTypeLibReferences( 
   System.int NCount,
   ref System.string BstrTlbRef
)
```

```

System.bool IRemoveUserTypeLibReferences( 
   System.int NCount,
   System.String^% BstrTlbRef
) 
```

#### Parameters

*NCount*
:   Number of user-specified type library references

*BstrTlbRef*
:   Array of strings of the user-specified type library references

#### Return Value

True if the user-specified type library references are removed, false if not

Remarks

Before calling this method, call [ISldWorks::GetUserTypeLibReferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.md) to get the value for NCount.

Any macro recorded after this method is called will not have references to the removed user-specified type libraries.

An add-in can use this method to remove its type library references when the add-in is unloaded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.md)  
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.md)  
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.md)  
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.md)
