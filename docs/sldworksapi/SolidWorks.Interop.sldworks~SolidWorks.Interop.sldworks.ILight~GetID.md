# GetID Method (ILight)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight~GetID`

Gets the light ID for this light feature.
Gets the light ID for this light feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As ILight
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

Light ID for this light feature

Remarks

A light ID:

- is unique within the document.
- is persistent across SOLIDWORKS sessions and never changes, even if you change the name of the light.
- can be used to identify a specific light in a document.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a light using its persistent reference ID, but you cannot get a light using this method.

Example

[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)  
[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)  
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)  
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILight Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md)  
[ILight Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight_members.md)
