# GetPartBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPartBox`

Gets the box enclosing the part.
Gets the box enclosing the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPartBox( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

```

Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Object
 
value = instance.GetPartBox(NoConversion)
```

```

System.object GetPartBox( 
   System.bool NoConversion
)
```

```

System.Object^ GetPartBox( 
   System.bool NoConversion
) 
```

#### Parameters

*NoConversion*
:   Convert to user units or not; true retains system units, false changes to user units

#### Return Value

Array of 6 doubles containing the 2 diagonal points that bound the part

Remarks

The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The X,Y,Z points returned are the lower- and upper-diagonal corners that bound the part with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the part and usually close to the minimum possible size, but this is not guaranteed.

Example

[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md)  
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md)  
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md)  
[IComponent2::GetBox Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.md)
