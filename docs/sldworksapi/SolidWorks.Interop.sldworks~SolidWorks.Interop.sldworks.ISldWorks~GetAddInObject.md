# GetAddInObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject`

Gets an add-in object for the specified SOLIDWORKS add-in.
Gets an add-in object for the specified SOLIDWORKS add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAddInObject( _
   ByVal Clsid As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Clsid As System.String
Dim value As System.Object
 
value = instance.GetAddInObject(Clsid)
```

```

System.object GetAddInObject( 
   System.string Clsid
)
```

```

System.Object^ GetAddInObject( 
   System.String^ Clsid
) 
```

#### Parameters

*Clsid*
:   GUID or ProgID of the add-in as registered with SOLIDWORKS (see Remarks)

#### Return Value

Your add-in object

Remarks

To specify Clsid with:

- a ProgID, read [Accessing SOLIDWORKS Add-in Objects](sldworksapiprogguide.chm::/Overview/Accessing_Add-ins.htm).
- a GUID, use curly brackets as in "{*GUID*}", or the string is interpreted as a ProgID.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::LoadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md)  
[ISldWorks::UnloadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn.md)
