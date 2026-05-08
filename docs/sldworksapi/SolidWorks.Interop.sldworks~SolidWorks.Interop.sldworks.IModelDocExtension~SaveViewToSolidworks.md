# SaveViewToSolidworks Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveViewToSolidworks`

Saves the specified named view of this model to SOLIDWORKS.
Saves the specified named view of this model to SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveViewToSolidworks( _
   ByVal ViewName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ViewName As System.String
Dim value As System.Boolean
 
value = instance.SaveViewToSolidworks(ViewName)
```

```

System.bool SaveViewToSolidworks( 
   System.string ViewName
)
```

```

System.bool SaveViewToSolidworks( 
   System.String^ ViewName
) 
```

#### Parameters

*ViewName*
:   Custom view name

#### Return Value

True if named view successfully saved, false if not

Remarks

For more information, read **SOLIDWORKS user-interface help > Detailing and Drawings > Drawings > Standard Drawing Views > Adding Named Views**.

Example

'VBA

Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks

    Set swApp = Application.SldWorks

    Dim swModel As ModelDoc2

    Set swModel = swApp.**ActiveDoc**

    swModel.ViewRotateplusz

    swModel.**GraphicsRedraw2**

    Dim newName As String

    newName = Format(Now, "YYYYMMDD-hhmmss")

    Dim bResult As Boolean

    swModel.**NameView** newName

    bResult = swModel.**Extension**.**SaveViewToSolidworks**(newName)

    Debug.Print "Saved view to SOLIDWORKS as """ & newName & """ == " & bResult

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
