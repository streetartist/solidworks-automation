# GetUserTypeLibReferenceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount`

Gets the number of user-specified type library references.
Gets the number of user-specified type library references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserTypeLibReferenceCount() As System.Integer
```

```

Dim instance As ISldWorks
Dim value As System.Integer
 
value = instance.GetUserTypeLibReferenceCount()
```

```

System.int GetUserTypeLibReferenceCount()
```

```

System.int GetUserTypeLibReferenceCount(); 
```

#### Return Value

Number of user-specified type library references

Remarks

Call this method before calling [ISldWorks::IGetUserTypeLibReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.md) to get the size of the array for that method.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.md)  
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.md)  
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.md)  
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.md)
