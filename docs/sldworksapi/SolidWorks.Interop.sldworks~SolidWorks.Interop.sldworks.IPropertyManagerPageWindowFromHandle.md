# IPropertyManagerPageWindowFromHandle Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle`

Allows you to access a PropertyManager page .NET control.
Allows you to access a [PropertyManager page](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) .NET control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPropertyManagerPageWindowFromHandle 
```

```

Dim instance As IPropertyManagerPageWindowFromHandle
```

```

public interface IPropertyManagerPageWindowFromHandle 
```

```

public interface class IPropertyManagerPageWindowFromHandle 
```

Remarks

The add-in that deploys a .NET control in a PropertyManager page must implement the event handler [IPropertyManagerPage2Handler8::OnWindowFromHandleControlCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnWindowFromHandleControlCreated.md). SOLIDWORKS populates the arguments of this handler when it attempts to create a .NET control on the PropertyManager page.

If SOLIDWORKS is unable to create a .NET control, it passes Status = false in the handler. When Status = false, the handler must return an action to take as defined in [swHandleWindowFromHandleCreationFailure\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHandleWindowFromHandleCreationFailure_e.html).

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

Example

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)  
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
