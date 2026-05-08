# RemoveUserTypeLibReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences`

Removes the user-specified type library references.
Removes the user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveUserTypeLibReferences( _
   ByVal VTlbRef As System.Object _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim VTlbRef As System.Object
Dim value As System.Boolean
 
value = instance.RemoveUserTypeLibReferences(VTlbRef)
```

```

System.bool RemoveUserTypeLibReferences( 
   System.object VTlbRef
)
```

```

System.bool RemoveUserTypeLibReferences( 
   System.Object^ VTlbRef
) 
```

#### Parameters

*VTlbRef*
:   Array of strings of the user-specified type library references

#### Return Value

True if the user-specified type library references are removed, false if not

Remarks

Any macro recorded after this method is called will not have references to the removed user-specified type libraries.

An add-in can use this method to remove its type library references when the add-in is unloaded.

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
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.md)  
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.md)
