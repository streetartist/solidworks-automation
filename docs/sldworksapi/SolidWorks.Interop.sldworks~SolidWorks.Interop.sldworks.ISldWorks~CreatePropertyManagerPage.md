# CreatePropertyManagerPage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage`

Creates a PropertyManager page.
Creates a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePropertyManagerPage( _
   ByVal Title As System.String, _
   ByVal Options As System.Integer, _
   ByVal Handler As System.Object, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Title As System.String
Dim Options As System.Integer
Dim Handler As System.Object
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.CreatePropertyManagerPage(Title, Options, Handler, Errors)
```

```

System.object CreatePropertyManagerPage( 
   System.string Title,
   System.int Options,
   System.object Handler,
   out System.int Errors
)
```

```

System.Object^ CreatePropertyManagerPage( 
   System.String^ Title,
   System.int Options,
   System.Object^ Handler,
   [Out] System.int Errors
) 
```

#### Parameters

*Title*
:   Title of the page

*Options*
:   Options as defined in [swPropertyManagerPageOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageOptions_e.html)

*Handler*
:   Pointer to the event handler for this page ([IPropertyManagerPage2Handler5](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5.md))

*Errors*
:   Status of the creation as defined in [swPropertyManagerPageStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageStatus_e.html)

#### Return Value

[PropertyManager page](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)

Remarks

Specify swPropertyManagerPageOptions\_e.swPropertyManagerOptions\_LockedPage in the Options parameter when you create your PropertyManager page. It is important that when a handler (such as [IPropertyManagerPage2Handler5::OnButtonPress](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnButtonPress.md) or [IPropertyManagerPage2Handler5::OnClose](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnClose.md)) is finished and control returns to SOLIDWORKS that the PropertyManager page is still there. If the PropertyManager page is not there, SOLIDWORKS might crash. Some methods try to close the PropertyManager page, but you can avoid this scenario by creating the PropertyManager page as Locked.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Example

[Cut Body In Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Create PropertyManager Page (VBA)](Create_PropertyManager_Page_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ICreatePropertyManagerPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.md)
