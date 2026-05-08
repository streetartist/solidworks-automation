# UserTypeLibReferences Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences`

Gets and sets the user-specified type library references.
Gets and sets the user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserTypeLibReferences As System.Object
```

```

Dim instance As ISldWorks
Dim value As System.Object
 
instance.UserTypeLibReferences = value
 
value = instance.UserTypeLibReferences
```

```

System.object UserTypeLibReferences {get; set;}
```

```

property System.Object^ UserTypeLibReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of the user-specified type library references

Remarks

An add-in can use this property to add its type library references after the add-in is loaded.

A user-specified type library first appears on the list of available references only after adding it and only after recording a macro.

User-specified type library references are not persistent across SOLIDWORKS sessions.

Only macros created after adding a user-specified type library reference can reference that type library.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

Example

[Add User-specified Type Library Reference (VBA)](Add_User-specified_Type_Library_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetUserTypeLibReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.md)  
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.md)  
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.md)  
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.md)
